import React, {Component, Fragment} from "react";
import {connect} from "react-redux";
import axios from 'axios';
import PropTypes from "prop-types";
import PostDetail from "./PostDetail"
import {getPosts} from "../../../actions/posts";
import {likePost} from "../../../actions/likes";
import Comments from "./Comments"
import './styles.scss'

export class Posts extends Component {
    static propTypes = {
        posts: PropTypes.array.isRequired,
        getPosts: PropTypes.func.isRequired,
        //deletePost: PropTypes.func.isRequired
    };

    state = {
        author: 0
    };


    render() {
        return (
            <Fragment>
                <br />
                <div class="container">
                    <div class="post">
                        {this.props.posts.map(post => (
                            <div class="post-body">
                                <PostDetail post={post} />
                                <Comments post={post} />
                            </div>
                        ))}
                    </div>
                </div>
            </Fragment >
        );
    }
}

const mapStateToProps = state => ({
    posts: state.posts.posts
});

export default connect(
    mapStateToProps,
    {getPosts}
)(Posts);
