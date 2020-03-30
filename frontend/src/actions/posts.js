import axios from 'axios';

import { GET_POSTS, ADD_POST, DELETE_POST } from './types';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// GET POSTS
export const getPosts = () => dispatch => {
    axios
    .get('/api/posts/')
    .then(res => {
        dispatch({
            type: GET_POSTS,
            payload: res.data
        });
    }).catch(err => console.log(err));
};

export const deletePost = id => dispatch => {
    axios
    .delete(`/api/posts/${id}/`)
    .then(res => {
        dispatch( {
            type: DELETE_POST,
            payload: id
        })
    })
    .catch(err => console.log(err));
}

// ADD POST
export const addPost = (post) => dispatch => {
    axios
    .post('/api/posts/', post)
    .then(res => {
        dispatch({
            type: ADD_POST,
            payload: res.data
        });
    }).catch(err => console.log(err));
};
