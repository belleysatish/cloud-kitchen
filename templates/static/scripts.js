// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const foodStyleList = document.getElementById('food-style-list');
    const categoryList = document.getElementById('category-list');
    const mealList = document.getElementById('meal-list');
    const itemList = document.getElementById('item-list');

    // Function to format JSON data for display
    const formatJson = (json) => {
        return `<pre>${JSON.stringify(json, null, 2)}</pre>`;
    };

    // Function to fetch and display data
    const fetchData = async (url, container) => {
        try {
            const response = await fetch(url);
            const data = await response.json();
            container.innerHTML = ''; // Clear previous content

            if (Array.isArray(data)) {
                data.forEach(item => {
                    const itemElement = document.createElement('div');
                    itemElement.classList.add('item');
                    itemElement.innerHTML = `
                        <h3>${item.name || 'No Name'}</h3>
                        <img src="${item.avatar || 'https://via.placeholder.com/150'}" alt="${item.name || 'No Name'}">
                        <p>${item.description || 'No Description'}</p>
                        <h4>Details:</h4>
                        ${formatJson(item.data)}
                    `;
                    container.appendChild(itemElement);
                });
            } else {
                const itemElement = document.createElement('div');
                itemElement.classList.add('item');
                itemElement.innerHTML = `
                    <h3>${data.name || 'No Name'}</h3>
                    <img src="${data.avatar || 'https://via.placeholder.com/150'}" alt="${data.name || 'No Name'}">
                    <p>${data.description || 'No Description'}</p>
                    <h4>Details:</h4>
                    ${formatJson(data.data)}
                `;
                container.appendChild(itemElement);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            container.innerHTML = '<p>Error loading data</p>';
        }
    };

    // Fetch and display data
    fetchData('/foodstyle/', foodStyleList);
    fetchData('/category/', categoryList);
    fetchData('/meal/', mealList);
    fetchData('/item/', itemList);
});
