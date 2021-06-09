const { clipboard, ipcRenderer, shell } = require('electron')

const clippingsList = document.getElementById('clippings-list');
const copyFromClipboardButton = document.getElementById('copy-from-clipboard');

const createClippingElement = (clippingText) => {
    const clippingElement = document.createElement('article');

    clippingElement.classList.add('clippings-list-item');

    clippingElement.innerHTML = `
      <div class="clipping-text" disabled="true"></div>
      <div class="clipping-controls">
        <button class="copy-clipping">&rarr; Clipboard</button>
        <button class="publish-clipping" disabled>Publish</button>
        <button class="remove-clipping">Remove</button>
      </div>
    `;

    clippingElement.querySelector('.clipping-text').innerText = clippingText;

    return clippingElement;
};

const addClippingToList = () => {
    const clippingText = clipboard.readText();
    const clippingElement = createClippingElement(clippingText);
    clippingsList.prepend(clippingElement);
};

const getBtnParent = ({ target }) => {
    return target.parentNode.parentNode
}

const getClippingText = clippingListItem => {
    return clippingListItem.querySelector('.clipping-text').innerText
}

const removeClipping = target => {
    target.remove()
}

const writeToClipboard = (clippingText) => {
    clipboard.writeText(clippingText);
}


/////////// events /////////
copyFromClipboardButton.addEventListener('click', addClippingToList)

clippingsList.addEventListener('click', e => {
    const hasClass = className =>
        e.target.classList.contains(className)

    const clippingListItem = getBtnParent(e)

    if (hasClass('remove-clipping')) removeClipping(clippingListItem);
    if (hasClass('copy-clipping')) writeToClipboard(getClippingText(clippingListItem));
    // if (hasClass('publish-clipping')) publishClipping(getClippingText(clippingListItem));
})


///////////// ipc //////////////
ipcRenderer.on('create-new-clipping', () => {
    addClippingToList();
    new Notification('Clipping Added', {
        body: `${clipboard.readText()}`
    });
});

ipcRenderer.on('write-to-clipboard', () => {
    const clipping = clippingsList.firstChild;
    writeToClipboard(getClippingText(clipping));
    new Notification('Clipping Copied', {
        body: `${clipboard.readText()}`
    });
});