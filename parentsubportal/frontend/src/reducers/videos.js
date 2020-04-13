import {
    GET_VIDEOS,
    POST_COMMENT,
    DELETE_COMMENT,
    UPDATE_COMMENT,
    GET_VIDEO,
} from "../actions/types.js";

const initialState = {
    videos: [],
    video: null,
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_VIDEOS: {
            return {
                ...state,
                videos: action.payload,
            };
        }
        case GET_VIDEO: {
            return {
                ...state,
                video: action.payload,
            };
        }
        case POST_COMMENT: {
            return {
                ...state,
                videos: state.videos.map((video) => {
                    if (video.id === action.payload.post) {
                        return {
                            ...video,
                            comments: video.comments.concat(action.payload),
                        };
                    }
                    return video;
                }),
            };
        }
        case DELETE_COMMENT: {
            return {
                ...state,
                video: state.videos.map((video) => {
                    if (video.id === action.payload.post) {
                        return {
                            ...video,
                            comments: video.comments.filter(
                                (comment) => comment.id != action.payload.id
                            ),
                        };
                    }
                    return video;
                }),
            };
        }
        case UPDATE_COMMENT: {
            return {
                ...state,
                videos: state.videos.map((video) => {
                    if (video.id === action.payload.post) {
                        return {
                            ...video,
                            comments: video.comments.filter(
                                (comment) => comment.id != action.payload.id
                            ),
                        };
                    }
                    return video;
                }),
            };
        }
        default:
            return state;
    }
}
