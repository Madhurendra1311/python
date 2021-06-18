const express = require('express')
const app = express()

app.use(express.json())

let books = [
    {
        title: "harry potter",
        author: "JK Rowling",
        year: 2001
    }
]

app.get('/book', (req, res) => {
    const title = req.body.title
    console.log(title);
    const getBooks = books.find(book => {
        return (book.title === title)
    })
    if (getBooks) {
        res.status(200).json(getBooks)
    }
    else {
        res.status(404).json({ error: "Erorr Fetching the User" })
    }
})

app.post('/create', (req, res) => {
    const title = req.body.title
    const author = req.body.author
    const year = req.body.year
    const book = { title, author, year }
    books.push(book)
    if (res.status(200)) {
        res.json({ status: "success", message: `${title} has been added to the array` })
    } else {
        res.status(404).json({ error: "No such book found" })
    }
})

app.delete('/delete', (req, res) => {
    const userbook = req.body.title
    const bookIndex = books.findIndex(item => {
        return (item.title === userbook)
    })
    if (bookIndex >= 0) {
        books.splice(bookIndex, 1);
        res.status(200).json({ status: "success", message: `${userbook} has been removed from the array` })
    }
    else {
        res.status(404).json({ error: "No such book found" })
    }
})

app.put('/edityear', (req, res) => {
    const index = books.findIndex(item => {
        return (item.title == req.body.book)
    })
    console.log(index);


    if (index >= 0) {
        const updatedYear = books[index];
        updatedYear.year = req.body.year
        res.status(200).json(updatedYear)
    }
    else {
        res.status(404).json({ error: "Updation of year failed" })
    }
})

app.listen(5000, () => {
    console.log('The server is up and running')
})