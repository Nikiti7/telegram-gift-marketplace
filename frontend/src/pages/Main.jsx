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
            .then(setProducts)
    }, []);

    const filtered = products.filter((p) =>
        String(p.price).includes(searchTerm.trim())
    );

    return (
        <div className="content">
            <Header balance={balance} setBalance={setBalance} />
            <main className="content">
                <FiltersNav searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
                <ProductGrid products={products} onClick={() => {
                    console.log('Card clicked!')
                }}/>
            </main>
            <Footer />
        </div>
    );
}
