const http = require('http');

const app = http.createServer((req, res) => {
    console.log(req.headers)
    let data = {
        date: new Date().getTime()
    }
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.write(JSON.stringify(data))
    res.end();
});

app.listen(8000, () => {
    console.log('Server is listening on port 8000')
})