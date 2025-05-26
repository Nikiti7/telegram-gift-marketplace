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
        setProducts([
            { id: 1, price: 3023 },
            { id: 2, price: 2500 },
            { id: 3, price: 1800 },
            { id: 4, price: 2200 },
        ]);
    }, []);

    const filtered = products.filter((p) =>
        String(p.price).includes(searchTerm.trim())
    );

    return (
        <div className="content">
            <Header balance={balance} setBalance={setBalance} />
            <main className="content">
                <FiltersNav searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
                <ProductGrid products={filtered} />
            </main>
            <Footer />
        </div>
    );
}
