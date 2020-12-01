const cheerio = require('cheerio')
const { url } = require('url')
const config = require('./config')

function findImg(dom, callback) {
    let $ = cheerio.load(dom)
    let urlObj = new URL(config.url)
    let baseUrl = urlObj.origin
    $('img').each((i, elem) => {
        let imgSrc = baseUrl + $(elem).attr('src').substr(1)    //problem
        callback(imgSrc, i)
        console.log(imgSrc)
    })
}

exports.findImg = findImg