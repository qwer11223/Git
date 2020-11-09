const fs = require('fs')
const http = require('http')
const host = '127.0.0.1'
const port = 8000

const server = http.createServer()

server.listen(port, host, () => {
    console.log(`The service is running at http://${host}:${port}`)
})

server.on('request', (request, response) => {
    console.log(request.url)
    let url = request.url

    if (url === '/favicon.ico') return

    if (url === '/') {
        var html = '<h1>Index of /</h1><ul>'

        fs.readdir(`.${url}`, 'utf8', (err, data) => {
            for (var i = 0; i < data.length; i++) {
                html += `<li><a href="${data[i]}">${data[i]}</a></li>`
            }

            response.setHeader('Content-Type', 'text/html')
            response.end(html + '</ul>')
        })
    }
    else {
        fs.readdir(`.${url}`, (err, data) => {
            if (err) {
                fs.readFile(`.${url}`, (err, data) => {
                    if (err)
                        response.end('Read file error!')
                    else
                        response.end(data)
                })
            }
            else {
                for (var i = 0; i < data.length; i++) {
                    html += `<li><a href="res_page/${data[i]}">${data[i]}</a></li>`
                }

                response.setHeader('Content-Type', 'text/html')
                response.end(html + '</ul>')
            }
        })
    }

})