import tabMarket from "../assets/icons/tab_market.svg";
import tabBasket from "../assets/icons/tab_basket.svg";

export default function Footer() {
  return (
    <footer className="footer">
      <nav className="footer__nav container">
        <button className="nav-tab" aria-label="Главная">
          <img src={tabMarket} alt="Маркет главная" />
        </button>
        <div className="menu">
          <button className="menu__item menu__basket" aria-label="Мои подарки">
            <img src={tabBasket} alt="Корзина" />
          </button>
        </div>
      </nav>
    </footer>
  );
}
