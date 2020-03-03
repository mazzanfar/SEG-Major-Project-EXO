import axios from 'axios';

import { GET_TOPICS } from './types';

// GET TOPICS
export const getTopics = () => dispatch => {
    axios
    .get('/api/topics/')
    .then(res => {
        dispatch({
            type: GET_TOPICS,
            payload: res.data
        });
    }).catch(err => console.log(err));
}
