// Load HTML content from a specified path and insert it into the given element
async function loadHTML(path, element) {
    try {
        const response = await fetch(path);
        const html = await response.text();
        element.innerHTML = html;
    } catch (error) {
        console.error('Error loading HTML:', error);
    }
}

// Load the header and footer when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    const headerElement = document.querySelector('header');
    const footerElement = document.querySelector('footer');
    const asideElement = document.querySelector('aside.sidebar');
    if (headerElement) {
        loadHTML('./subpagetemplate/headerEndProblem.html', headerElement);
    }
    if (footerElement) {
        loadHTML('./subpagetemplate/footer.html', footerElement);
    }
    if (asideElement) {
        loadHTML('./subpagetemplate/asideEndProblem.html', asideElement);
    }

});
