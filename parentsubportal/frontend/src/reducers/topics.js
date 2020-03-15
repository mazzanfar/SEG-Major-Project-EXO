import { GET_TOPICS, ADD_TOPIC } from '../actions/types.js';

const initialState = {
    topics: []
}

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_TOPICS:
            console.log(action.type)
            return {
                ...state,
                topics: action.payload
            };
        case ADD_TOPIC:
            return {
                ...state,
                topics: [ ...state.topics, action.payload]
            };
        default:
            return state;
    }
}
