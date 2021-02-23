const fs = require('fs')
const http = require('http')
const host = '127.0.0.1'
const port = 8000
const basePath = './www'

const server = http.createServer()

server.listen(port, host, () => {
    console.log(`The service is running at http://${host}:${port}`)
})

server.on('request', (request, response) => {
    let url = decodeURI(request.url)

    console.log(url)

    var html = `<h1>Index of ${url}</h1><ul>`

    if (url === '/favicon.ico') return

    if (url === '/') {
        fs.readdir(`${basePath}`, 'utf8', (err, data) => {
            if (err) {
                response.end('Directory does not exist!')
                return false
            }
            for (var i = 0; i < data.length; i++) {
                html += `<li><a href="${data[i]}">${data[i]}</a></li>`
            }

            response.setHeader('Content-Type', 'text/html')
            response.end(html + '</ul>')
        })
    }
    else {
        fs.readdir(`${basePath}${url}`, (err, data) => {
            if (err) {
                fs.readFile(`${basePath}${url}`, (err, data) => {
                    if (err)
                        response.end('Read file error!')
                    else
                        response.end(data)
                })
            }
            else {
                for (var i = 0; i < data.length; i++) {
                    html += `<li><a href="${url}/${data[i]}">${data[i]}</a></li>`
                }

                response.setHeader('Content-Type', 'text/html')
                response.end(html + '</ul>')
            }
        })
    }

})