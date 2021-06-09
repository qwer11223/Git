const { menubar } = require('menubar')
const { globalShortcut, Menu } = require('electron')

const mb = menubar({
    index: `${__dirname}/index.html`,
    preloadWindow: true,
    browserWindow: {
        webPreferences: {
            contextIsolation: false,
            nodeIntegration: true
        }
    },
    tooltip: 'clipmater-9000',
    icon: 'icons/clip32.ico',
    showDockIcon: false
})

mb.on('ready', () => {
    const secondaryMenu = Menu.buildFromTemplate([
        {
            label: 'Quit',
            click() { mb.app.quit(); },
            accelerator: 'Q'
        },
    ]);

    mb.tray.on('right-click', () => {
        mb.tray.popUpContextMenu(secondaryMenu);
    });


    //////// globalShortcut ///////////
    const createClipping = globalShortcut.register('CmdOrCtrl+Alt+1', () => {
        mb.window.webContents.send('create-new-clipping');
    });

    const writeClipping = globalShortcut.register('CmdOrCtrl+Alt+2', () => {
        mb.window.webContents.send('write-to-clipboard');
    });
})
