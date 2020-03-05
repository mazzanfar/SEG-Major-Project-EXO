import React, {Component, Fragment} from 'react'
import axios from 'axios'
import PropTypes from "prop-types";
import { connect } from 'react-redux'
import { postComment } from "../../../actions/comments"
import { getPosts } from "../../../actions/posts";
import './styles.scss'

// TODO: pass posts in ways besides props
export class Comments extends Component {
    constructor(props) {
        super(props)

        this.state = {
            comment: "",
            author: null
        }
    }
    static propTypes = {
        postComment: PropTypes.func.isRequired,
        getPosts: PropTypes.func.isRequired
    };

    onFieldChange(fieldName) {
        return function (event) {
            this.setState({[fieldName]: event.target.value});
        }
    }
    componentDidMount() {
        this.props.getPosts();
        axios
        .get(`/api/auth/user`)
        .then(res => {
            const author = res.data.id
            this.setState({author});
        })
        .catch(err => console.log(err));
    }

    onSubmit(e) {
        e.preventDefault();
        const variables = {
            content: this.state.comment,
            post: this.props.post.id,
            author: this.state.author
        }
        this.props.postComment(variables)
        this.setState({comment: ""});
    }

    render() {
            return (
            <Fragment>
                <div class="post-comment-box">
                   <div class="user"><img src="https://bootdey.com/img/Content/avatar/avatar6.png"/></div>
                   <div class="input">
                    <form style={{ display:'flex'}} onSubmit={e => this.onSubmit(e)}>
                         <div class="input-group">
                            <input 
                                class="form-control rounded-corner"
                                style={{width: '100%', borderRadius: '5px'}} 
                                onChange={this.onFieldChange('comment').bind(this)}
                                value = {this.state.comment}
                                placeholder="Leave a comments"
                            />
                            <span class="input-group-btn p-l-10">
                            <button class="btn btn-primary f-s-12 rounded-corner">Comment</button>
                            </span>
                         </div>
                      </form>
                   </div>
                </div>
                <div>

                    <h1 class="comments-title">Comments ({this.props.post.total_comments})</h1>
                    {/* Comment Lists */}
                    {this.props.post.comments.map(comment => (
                        <div class="be-comment-block">
                            <div class="be-comment">
                                <div class="be-img-comment">	
                                    <a href="blog-detail-2.html">
                                        <img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="" class="be-ava-comment"/>
                                    </a>
                                </div>
                                <div class="be-comment-content">
                                        <span class="be-comment-name">
                                            <a href="blog-detail-2.html">Some Name</a>
                                            </span>
                                        <span class="be-comment-time">
                                            <i class="fa fa-clock-o"></i>
                                            May 27, 2015 at 3:14am
                                        </span>
                                    <p class="be-comment-text">{comment.content}</p>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </Fragment>
        );
    }
}

const mapStateToProps = state => ({
    posts: state.posts.posts
});

export default connect(
    mapStateToProps,
    { postComment, getPosts}
)(Comments);
