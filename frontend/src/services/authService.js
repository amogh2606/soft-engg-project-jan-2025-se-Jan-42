import { getUser, loginUser, logoutUser } from '@/api';

export async function performLogin(email, password) {
    try {
        await loginUser(email, password);
        const userResponse = await getUser();
        return userResponse.data;
    } catch (error) {
        if (error.response) {
            throw new Error(error.response.data?.message || error.message);
        }
        throw error;
    }
}

export async function performLogout() {
    try {
        await logoutUser();
    } catch (error) {
        if (error.response) {
            throw new Error(error.response.data?.message || error.message);
        }
        throw error;
    }
}
