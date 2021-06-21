const http = require('http')

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.write('Welcome to My first Node server!')
    res.end()
});

app.listen(5000, () => {
	console.log('Server is listening on port 5000')
}); 
