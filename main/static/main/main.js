document.addEventListener('DOMContentLoaded', function() {
    const parts = document.querySelectorAll('.part');
    const description = document.querySelector('.description');

    parts.forEach(part => {
        part.addEventListener('mouseover', function() {
            const descriptionData = this.getAttribute('description-data');
            description.innerHTML = descriptionData;
            description.style.display = 'block';
        });

        part.addEventListener('mouseout', function() {
            description.style.display = 'none';
        });
    });
});