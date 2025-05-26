import presentImg from "../assets/present_photo.png";
import sprite from "../assets/icons/sprite.svg";

export default function ProductCard({ price }) {
  return (
    <article className="present">
      <img className="present__img" src={presentImg} alt="" />
      <button className="present__favourite">
        <svg>
          <use href={`${sprite}#icon-favourite`}></use>
        </svg>
      </button>
      <p className="present__price">{price} руб</p>
    </article>
  );
}
