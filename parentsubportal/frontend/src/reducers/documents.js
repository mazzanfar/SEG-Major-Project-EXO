import { GET_DOCUMENTS } from '../actions/types.js';

const initialState = {
    documents: []
}

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_DOCUMENTS:
            return {
                ...state,
                documents: action.payload
            };
        default:
            return state;
    }
}
