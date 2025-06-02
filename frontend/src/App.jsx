import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Profile from "./pages/Profile";
import WelcomeModal from './components/WelcomeModal/WelcomeModal';
import {useState} from "react";


export default function App() {
    const [isWelcomeOpen, setIsWelcomeOpen] = useState(true);


    return (
        <div className="app">
            <WelcomeModal
                isOpen={isWelcomeOpen}
                onClose={() => setIsWelcomeOpen(false)}
            />
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/profile" element={<Profile />} />
            </Routes>
        </div>

);
}
