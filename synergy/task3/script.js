// Массив с картинками
const images = [
    'img/1.jpg',
    'img/2.jpg',
    'img/3.jpg',
    'img/4.jpg',
    'img/5.jpg'
];

const slider1 = document.querySelector('.slider-1 img');
const slider2 = document.querySelector('.slider-2 img');
const slider3 = document.querySelector('.slider-3 img');
const squares = document.querySelectorAll('.square');
const numbers = document.querySelector('.numbers');
const arrowLeft = document.querySelector('.arrow-left');
const arrowRight = document.querySelector('.arrow-right');

let currentIndex = 0;

// Функция обновления слайдера
function updateSlider() {
    slider2.src = images[currentIndex];

    let leftIndex = (currentIndex - 1 + images.length) % images.length;
    slider1.src = images[leftIndex];

    let rightIndex = (currentIndex + 1) % images.length;
    slider3.src = images[rightIndex];

    numbers.textContent = `${currentIndex + 1}/${images.length}`;

    squares.forEach((square, index) => {
        if (index === currentIndex) {
            square.classList.add('active');
        } else {
            square.classList.remove('active');
        }
    });
}

// Переключение слайдера стрелками
arrowRight.addEventListener('click', function () {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
});

arrowLeft.addEventListener('click', function () {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
});

// Переключение слайдера квадратами
squares.forEach((square, index) => {
    square.addEventListener('click', function () {
        currentIndex = index;
        updateSlider();
    });
});


const modal = document.getElementById('modal');
const modalImage = document.getElementById('modalImage');
const closeBtn = document.getElementById('closeModal');
const sliderCenter = document.querySelector('.slider-2');

// Открытие картинки на весь экран
sliderCenter.addEventListener('click', function () {
    modalImage.src = slider2.src;
    modal.classList.add('show');
});

closeBtn.addEventListener('click', function () {
    modal.classList.remove('show');
});

modal.addEventListener('click', function (e) {
    if (e.target === this) {
        modal.classList.remove('show');
    }
});

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        modal.classList.remove('show');
    }
});

// Инициализация функции
updateSlider();