字符I/O :

* int getchar() ：读取指定输入的下一个字符
* int putchar(int)：把指定字符写入指定输出中

字符串I/O ：

* char * gets(char *)：读取整行输入，直至遇到换行符；丢弃换行符，存储其余字符，并在字符末尾添加一个空字符。
* int puts(const char *)：把字符串写入指定输出中,并添加换行符
* scanf()：遇到空白字符（空行、空格、制表符、或换行符）作为字符串结束，不包括空白字符

文件I/O :

* getc(fp)：从fp指定的文件中获取一个字符
* putc(char ch, FILE* fpout)：把字符ch放入FILE指针fpout指定的文件中
* char * fgets(buf, STLEN, fp) ： 第二个参数读入n-1个字符，保留换行符，第3个参数指明要读入的文件,并在字符末尾添加一个空字符
* int fputs(const cahr* buf, FILE * fp)：把第1个参数指向的字符串写入指定流,不添加换行符
* fprintf(FILE *fp, ...) ：格式化输出到文件指针fp
* fscanf(FILE *fp, ...)

二进制I/O (p429) : 

* fwrite(ptr, size, nmemb, fp)
* fread(ptr, size, nmemb, fp)

字符串函数 (p702) :

* strlen(char *s)：返回字符串s中的字符数(末尾空字符除外)
* strcat(str1,str2)：s2拼接到s1字符串后面，返回s1
* strncat(s1,s2,n)：s2的n个字符（或拷贝到s2的空字符为止）拼接到s1字符串后面，返回s1
* strcmp(s1,s2)：通过字符编码值比较字符，相同返回0，s1<s2返回小于0的值，s1>s2返回大于0的值
* strcpy(s1,s2)：s2指向的字符串拷贝到s1指向的位置，返回s1
* strncpy(s1,s2,n)：s2指向的n个字符拷贝到s1指向的位置，返回s1
* sprintf(**char \*str, const char \*format, ...**)：发送格式化输出到 **str** 所指向的字符串







