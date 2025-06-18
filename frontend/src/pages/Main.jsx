import { useState, useEffect } from "react";
import Header from "../components/Header";
import FiltersNav from "../components/FiltersNav";
import ProductGrid from "../components/ProductGrid";
import Footer from "../components/Footer";
import "../styles/reset.css";
import "../styles/index.css";
import "../styles/filters.css";

export default function Main() {
    const [balance, setBalance] = useState(0);
    const [searchTerm, setSearchTerm] = useState("");
    const [products, setProducts] = useState([]);
		
    useEffect(() => {
      fetch("http://localhost:4000/api/gifts")
        .then(res => res.json())
        .then(data => {
            console.log("Fetched products:", data);
            if (Array.isArray(data)) {
                setProducts(data);
            } else {
                console.error("Expected array, got:", data);
                setProducts([]);
            }
        })
        .catch(err => {
            console.error("Failed to fetch products:", err);
        });
    }, []);


    const filtered = Array.isArray(products)
      ? products.filter((p) =>
        String(p.price).includes(searchTerm.trim())
      )
    : [];


    return (
        <div className="content">
            <Header balance={balance} setBalance={setBalance} />
            <main className="content">
                <FiltersNav searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
                <ProductGrid products={filtered} onClick={() => {
                    console.log('Card clicked!')
                }}/>
            </main>
            <Footer />
        </div>
    );
}
