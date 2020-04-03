import { GET_PDFS } from "../actions/types.js";

const initialState = {
    pdfs: [],
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_PDFS: {
            return {
                ...state,
                pdfs: action.payload,
            };
        }
        default:
            return state;
    }
}
