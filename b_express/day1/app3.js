const http = require('http')

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    res.write(
        '<html lang="en"><head><title>My Node Server</title></head><body><h1>Welcome to My Server</h1></body></html>'
    )
    res.end();
});

app.listen(5000, () => {
    console.log('Server is listening on port 5000')
});