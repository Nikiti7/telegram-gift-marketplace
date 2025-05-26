import {Link} from "react-router-dom";

export default function Profile() {
    return (
        <>
            <h1>Профиль</h1>;
            <Link to="/" className="profile">
                <h1>Главная</h1>
            </Link>
        </>
        )

}
