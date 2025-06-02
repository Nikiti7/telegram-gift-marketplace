import presentImg from "../assets/welcomeAssets/images/present_frog.png";
import sprite from "../assets/icons/sprite.svg";

export default function ProductCard({ price }) {
  return (
    <article className="present">
      <div className="present__info">
          <img className="present__img" src={presentImg} alt="Подарок с изображением лягушки" />
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
  );
}
