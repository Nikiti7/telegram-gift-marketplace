const filters = document.getElementById('filtersModal');
const openFilter = document.getElementById('open-filters');
const closeFilter = document.getElementById('close-filters');


openFilter.addEventListener('click', () => {filters.classList.toggle('active')})
closeFilter.addEventListener('click', () => {filters.classList.toggle('active')})

const mainFilters = document.querySelectorAll('.main-filter');
const slider = document.querySelector('.slider');

mainFilters.forEach((filter, index) => {
  filter.addEventListener('click', () => {
    mainFilters.forEach(f => f.classList.remove('active'));
    filter.classList.add('active');
    slider.style.transform = `translateX(${index * 90}%)`;
  });
});

const wordFilters = document.querySelectorAll('.word-filter');

wordFilters.forEach((filter) => {
  filter.addEventListener('click', () => {
    wordFilters.forEach(f => f.classList.remove('active'));
    filter.classList.add('active');
  });
});
