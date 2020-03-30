import { GET_POSTS, ADD_POST, DELETE_POST, LIKE_POST } from '../actions/types.js';

const initialState = {
    posts: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_POSTS: {
            console.log(action.type)
            return {
                ...state,
                posts: action.payload
            };
        }
        case ADD_POST:
            return {
                ...state,
                posts: [ ...state.posts, action.payload]
            };
        case DELETE_POST:
            return {
                ...state,
                posts: state.posts.filter(post => post.id !== action.payload)
            }
        case LIKE_POST:
              return {
                ...state,
                posts: state.posts.map(post => {
                  if (post.id === action.payload.post) {
                    return {
                        ...post,
                        likes_count: post.likes_count + 1
                    }
                  }
                  return post;
                })
              };
        default:
            return state;
    }
}
