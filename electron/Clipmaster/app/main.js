const path = require('path')
const { app, Menu, Tray, clipboard, globalShortcut, Notification } = require('electron')

let tray = null
const clippings = []

const updateMenu = () => {  //更新右键菜单
    const menu = Menu.buildFromTemplate([
        {
            label: 'Create New Clipping',
            click() { addClipping() },
            accelerator: 'C'
        },
        { type: 'separator' },
        ...clippings.slice(0, 10).map(createClippingMenuItem),   //创建剪切项 //保留10项
        { type: 'separator' },
        {
            label: 'Quit',
            click() { app.quit() },
            accelerator: 'Q'
        }
    ])

    tray.setContextMenu(menu)
}

const addClipping = () => { //读取剪切板文本内容
    const clipping = clipboard.readText()
    if (clippings.includes(clipping)) return //防止添加重复项
    clippings.unshift(clipping)
    updateMenu()
    return clipping
}

const createClippingMenuItem = (clipping, index) => {
    return {
        label: clipping.length > 20 ? clipping.slice(0, 20) + '...' : clipping,
        click() { clipboard.writeText(clipping) },
        accelerator: `CommandOrControl+${index}`
    }
}

app.on('ready', () => {
    if (app.dock) app.dock.hide()    // hide mac_os dock ico

    tray = new Tray('icons/clip32.ico')

    if (process.platform === 'win32')
        tray.on('click', () => { tray.popUpContextMenu() })  //popup menu

    ///////// 注册全局快捷键 ////////
    const activationShortcut = globalShortcut.register(
        'CommandOrControl+Shift+P',
        () => { tray.popUpContextMenu() }
    )
    if (!activationShortcut) //注册失败electron返回虚值
        console.error('Global activation shortcut failed to register')


    const newClippingShortcut = globalShortcut.register(
        'CommandOrControl+Shift+Q',
        () => {
            const c = addClipping()
            if (c) showNotification()
        }
    )
    if (!newClippingShortcut) //注册失败electron返回虚值
        console.error('Global activation shortcut failed to register')

    //////////////////////////////

    updateMenu()

    tray.setToolTip('Clipmaster')

})

const showNotification = () => {
    const title = 'clipping'
    const body = 'Clipping Added'

    new Notification({ title: title, body: body }).show()
}