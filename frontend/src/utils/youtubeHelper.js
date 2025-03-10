export function getYoutubeVideoId(url) {
    try {
        const parsedUrl = new URL(url);
        const pathSegments = parsedUrl.pathname.split('/').filter(p => p);

        // Handle youtu.be URLs
        if (parsedUrl.hostname.includes('youtu.be')) {
            return pathSegments[0] || null;
        }

        // Handle attribution_link URLs
        if (pathSegments[0] === 'attribution_link') {
            const uParam = parsedUrl.searchParams.get('u');
            if (uParam) {
                const decodedUrl = decodeURIComponent(uParam);
                return getYoutubeVideoId(new URL(decodedUrl, parsedUrl.origin).href);
            }
        }

        // Handle paths like /shorts/, /live/, /embed/, /v/, /e/
        const directPaths = ['shorts', 'live', 'embed', 'v', 'e'];
        if (pathSegments.length > 1 && directPaths.includes(pathSegments[0])) {
            return pathSegments[1];
        }

        // Handle /watch path variations
        if (pathSegments[0] === 'watch') {
            return pathSegments.length > 1
                ? pathSegments[1]
                : parsedUrl.searchParams.get('v');
        }

        // Check for video ID in query parameters
        return parsedUrl.searchParams.get('v');
    } catch (error) {
        return null;
    }
}

export function getYoutubeEmbedUrlFromUrl(url) {
    const videoId = getYoutubeVideoId(url);
    return `https://www.youtube.com/embed/${videoId}`;
}

export function getYoutubeEmbedUrl(videoId) {
    return `https://www.youtube.com/embed/${videoId}`;
}

