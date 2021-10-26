// ArrayBuffer 代表内存中的一段二进制数据，除了ArrayBuffer.slice()方法，只能通过“视图”进行操作(TypedArray视图、DataView视图)

var buf = new ArrayBuffer(16); //生成一段16 Byte的内存区域，每个字节默认为0

// byteLength返回分配的内存区域字节长度
if (buf.byteLength == 16) {
    console.log(buf.byteLength + "Byte");
}

//-------- TypedArry视图 ---------------
//TypedArry只能解析小端字节序，自定义字节序可使用DataView
console.log('############ TypedArry视图 #################');

//创建一个指向buf的int32视图(32 bit->4 Byte)，开始于字节0，直到缓冲区末尾
var int32View = new Int32Array(buf);
for (let i = 0; i < int32View.length; i++) {    //4
    int32View[i] = i * 2;
    console.log(`int32View[${i}]: ${int32View[i]}`);
}

console.log('\n');

var int16View = new Int16Array(buf);
for (let i = 0; i < int16View.length; i++) {   //8
    console.log(`int16View[${i}]: ${int16View[i]}`);
}


/* case1:字节序 */
var buffer = new ArrayBuffer(4);
var v1 = new Uint8Array(buffer);
console.log(v1.BYTES_PER_ELEMENT + " Byte");

v1[0] = 2;
v1[1] = 1;
v1[2] = 3;
v1[3] = 7;
/* / v1[3] / v1[2] / v1[1] / v1[0] / */
/* /   7   /   3  /    1  /    2  / */

var uInt16View = new Uint16Array(buffer);
console.log(uInt16View[0]); //258

uInt16View[0] = 255;    //字节变为 [0xFF,0x00,0x03,0x07]
uInt16View[0] = 0xff05; //字节变为 [0x05,0xFF,0x03,0x07]
uInt16View[1] = 0x0210; //字节变为 [0x05,0xFF,0x10,0x02]

//溢出
console.log('--------------- 溢出 ----------------');
var uint8 = new Uint8Array(1);

uint8[0] = 256; //正向溢出1：数据类型最小值0+余数1-1 = 0
console.log('正向溢出: ' + uint8[0]);

uint8[0] = -1; //负向溢出1：数据类型最大值255-余数1+1 = 255
console.log('负向溢出: ' + uint8[0]);

console.log('--------------- TypedArray properties ----------------');
console.log('TypedArray.prototype.buffer(内存区域对应的ArrayBuffer对象): ' + uInt16View.buffer);
console.log('TypedArray.prototype.byteLength(TypedArray数组占据的内存长度(Byte)): ' + uInt16View.byteLength);
console.log('TypedArray.prototype.byteOffset(TypedArray数组从底层ArrayBuffer对象的哪个字节开始): ' + uInt16View.byteOffset);
console.log('TypedArray.prototype.length(TypedArray数组含有多少个成员): ' + uInt16View.length);

console.log('--------------- TypedArray methods ----------------');
console.log('TypedArray.prototype.set() 将一段内存完全复制到另一段内存');
var a = new Uint8Array(8);
var b = new Uint8Array(8);
b.set(a); //复制a数组的内容到b数组

//生成TypedArray的三种方式
//1. 
let tarr = new Uint8Array([1, 2, 3]);
//2.
let tarr1 = Uint8Array.of(1, 2, 3);
//3.
let tarr2 = new Uint8Array(3);
tarr2[0] = 1;
tarr2[1] = 2;
tarr2[2] = 3;


console.log();

/* case2:判断大小端字序 */
function getPlatformEndianess() {
    const BIG_ENDIAN = Symbol('BIG_ENDIAN');
    const LITTLE_ENDIAN = Symbol('LITTLE_ENDIAN');

    let arr32 = Uint32Array.of(0x12_345_678);
    let arr8 = new Uint8Array(arr32.buffer);
    switch (arr8[0] * 0x1_000_000 + arr8[1] * 0x10_000 + arr8[2] * 0x1_00 + arr8[3]) {
        case 0x12345678:
            return BIG_ENDIAN;
        case 0x78563412:
            return LITTLE_ENDIAN;
        default:
            throw new Error('Unknow endianness');
    }
}

console.log(getPlatformEndianess());

console.log('--------------- 复合视图 ----------------');
var buffer0 = new ArrayBuffer(24); //24Byte

var idView = new Int32Array(buffer0, 0, 1); //4Byte
var userView = new Uint8Array(buffer0, 4, 16); //字节4-字节19  
var aMoutView = new Uint32Array(buffer0, 20, 1);
//等同于以下c数据结构
/*
    struct someStruct{
        usigned long id;
        char username[16];
        float aMountView;
    }
*/

//DataView视图
console.log('############ DataView视图 #################');
var dataViewBuffer = new ArrayBuffer(24);
var dv = new DataView(dataViewBuffer);
dv.setInt8(0, 12, true);  //写入内存; true：大端写入（默认），false | undefine：小端写入
console.log(dv.getUint8(0));   //读取内存; 从第一个字节读取一个8位无符号整数

//判断计算机使用的字节序

var LE = (function () {
    let buffer = new ArrayBuffer(2);
    new DataView(buffer).setInt16(0, 256, true);
    return new Int16Array(buffer)[0] == 256;    //true 为小端字序
})();
console.log(LE);
