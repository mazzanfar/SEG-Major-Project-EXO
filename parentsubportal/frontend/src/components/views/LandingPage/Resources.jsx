import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import { Item } from "semantic-ui-react";
import axios from "axios";
import PropTypes from "prop-types";
import PostDetail from "./PostDetail";
import { getPosts } from "../../../actions/posts";
import Comments from "./Comments";

export class Resources extends Component {
    static propTypes = {
        posts: PropTypes.array.isRequired,
        getPosts: PropTypes.func.isRequired,
        //deletePost: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getPosts();
    }

    state = {
        author: 0,
    };
    render() {
        return (
            <Fragment>
                <br />
                {this.props.posts.map((post) => (
                    <Item.Group>
                        <PostDetail postId={post.id} />
                        <Comments post={post} />
                    </Item.Group>
                ))}
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({
    posts: state.posts.posts,
});

export default connect(mapStateToProps, { getPosts })(Posts);
