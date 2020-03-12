import { LIKE_POST } from '../actions/types.js';

const initialState = {
    posts: []
}

export default function(state = initialState, action) {
    switch(action.type) {
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
