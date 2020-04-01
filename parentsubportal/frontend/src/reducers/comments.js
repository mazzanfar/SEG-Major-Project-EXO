import { GET_COMMENTS, POST_COMMENT } from "../actions/comments";

const initialState = {
    comments: [],
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_COMMENTS: {
            console.log(action.payload);
            return {
                ...state,
                comments: action.payload,
            };
        }
        case POST_COMMENT:
            return {
                ...state,
                comments: [...state.comments, action.payload],
            };
        default:
            return state;
    }
}
