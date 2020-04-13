import {
    GET_PDFS,
    POST_COMMENT,
    DELETE_COMMENT,
    UPDATE_COMMENT,
    GET_PDF,
} from "../actions/types.js";

const initialState = {
    pdfs: [],
    pdf: null,
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_PDFS: {
            return {
                ...state,
                pdfs: action.payload,
            };
        }
        case GET_PDF: {
            return {
                ...state,
                pdf: action.payload,
            };
        }
        case POST_COMMENT: {
            return {
                ...state,
                pdfs: state.pdfs.map((pdf) => {
                    if (pdf.id === action.payload.post) {
                        return {
                            ...pdf,
                            comments: pdf.comments.concat(action.payload),
                        };
                    }
                    return pdf;
                }),
            };
        }
        case DELETE_COMMENT: {
            return {
                ...state,
                pdfs: state.pdfs.map((pdf) => {
                    if (pdf.id === action.payload.post) {
                        return {
                            ...pdf,
                            comments: pdf.comments.filter(
                                (comment) => comment.id != action.payload.id
                            ),
                        };
                    }
                    return pdf;
                }),
            };
        }
        case UPDATE_COMMENT: {
            return {
                ...state,
                pdfs: state.pdfs.map((pdf) => {
                    if (pdf.id === action.payload.post) {
                        return {
                            ...pdf,
                            comments: pdf.comments.filter(
                                (comment) => comment.id != action.payload.id
                            ),
                        };
                    }
                    return pdf;
                }),
            };
        }
        default:
            return state;
    }
}
