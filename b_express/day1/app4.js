const http = require('http')
const fs = require('fs')

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/json' })
    fs.readFile('persons.json', (err, data) => {
        res.write(data)
        res.end()
    })

})
app.listen(8000, () => {
    console.log('Server is listening on port 8000')
})