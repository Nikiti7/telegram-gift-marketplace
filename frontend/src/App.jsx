import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Profile from "./pages/Profile";

export default function App() {
  return (
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
  );
}
