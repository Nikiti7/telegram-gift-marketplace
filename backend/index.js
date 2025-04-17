import express from 'express';

// Локальный сервер
const app = express(); 

app.use(express.json()); 

app.post('/web-data', (req, res) => {
	try {
		return res.status(200).json({});
	} catch(e) {
		return res.status(500).json({});
	}
});


const PORT = 8000;

app.listen(PORT, () => console.log('server started on PORT' + PORT));