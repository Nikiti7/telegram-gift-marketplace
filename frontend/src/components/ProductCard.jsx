import presentImg from "../assets/welcomeAssets/images/present_frog.png";
import sprite from "../assets/icons/sprite.svg";
import CardInfo from "./CardInfo/CardInfo";
import {useState} from "react";

export default function ProductCard({price, id, model, symbol, ...otherProps}) {
    const [isInfoOpen, setIsInfoOpen] = useState(false)
    return (
        <>
            <article className="present" onClick={() => {
                console.log('Card clicked!');
                setIsInfoOpen(true)
            }}>
                <div className="present__info">
                    <img className="present__img" src={presentImg} alt="Подарок с изображением лягушки"/>
                    <div className="present__do">
                        <button className="present__favourite icons-bg" aria-label="Добавить в избранное">
                            <svg aria-hidden="true">
                                <use href={`${sprite}#icon-favourite`}></use>
                            </svg>
                        </button>
                        <button className="present__basket icons-bg" aria-label="Добавить в корзину">
                            <svg aria-hidden="true">
                                <use href={`${sprite}#icon-basket`}></use>
                            </svg>
                        </button>
                    </div>
                </div>
                <p className="present__price">{price} руб</p>
            </article>
            <CardInfo
                isOpen={isInfoOpen}
                onClose={() => setIsInfoOpen(false)}
                model={model}
                symbol={symbol}
                presentImg={presentImg}
                price={price}
            >

            </CardInfo>
        </>
    );
}
