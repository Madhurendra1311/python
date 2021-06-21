const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' })
        res.write('<html><head><title>Welcome Node.JS</title></head><body><h1>Welcome to World of Node JS</h1><a href="/about">About</a><br><a href="/data">Download CSV</a></body></html>')
        res.end()
    }
    else if (req.url === '/about') {
        res.writeHead(200, { 'Content-Type': 'text/html' })
        res.write('<h1>This is the about page</h1>')
        res.end()
    }
    else if (req.url === '/data') {
        res.setHeader("Content-Type", "text/csv")
        res.setHeader("Content-Disposition", "attachment; filename=userdata.csv")
        res.writeHead(200);
        res.write(`id, name, email, phone\n 1, Madhu, kmadhu1311@gmail.com, 8709181793\n 2, Madhu K, kmadhu1311@gmail.com, 8709181793`)
        res.end()
    }
    else {
        res.writeHead(404, { 'Content-Type': 'text/html' })
        res.write('<h1>404 Page not Found</h1>')
        res.end()
    }
});

server.listen(8000, () => {
    console.log('Server is listening on port 8000')
});