var BASE_URL = 'http://www.foxgami.com/api';

export default {
    get(path) {
        return fetch(BASE_URL + path).then((response) => {
            return response.json();
        });
    }
}