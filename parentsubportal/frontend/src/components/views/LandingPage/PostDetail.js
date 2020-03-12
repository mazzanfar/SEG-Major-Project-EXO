import React, {Component, Fragment} from "react";
import {connect} from "react-redux";
import {Button, Icon, Label} from "semantic-ui-react";
import {likePost} from "../../../actions/likes"

export class PostDetail extends Component {

    handleLikePost() {
        const like = {"post": this.props.post.id, "user": 14, "vote_type": "like"}
        this.props.likePost(like)
    }

    render() {
        return (
            <Fragment>
                <div class="post-header">
                    <span class="userimage"><img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="" /></span>
                    <span class="username"><a href="javascript:;">John Smith</a> <small></small></span>
                    <span class="float-right text-muted">{this.props.post.views} Views</span>
                </div>
                <div class="post-content">
                    <p>
                        {this.props.post.content}
                    </p>
                </div>
                <div class="post-likes">
                    <div class="stats-right">
                        <span class="stats-text">{}</span>
                        <span class="stats-text">{this.props.post.total_comments} Comments</span>
                    </div>
                    <div class="stats">
                        <span class="fa-stack fa-fw stats-icon">
                            <i class="fa fa-circle fa-stack-2x text-danger"></i>
                            <i class="fa fa-heart fa-stack-1x fa-inverse t-plus-1"></i>
                        </span>
                        <span class="fa-stack fa-fw stats-icon">
                            <i class="fa fa-circle fa-stack-2x text-primary"></i>
                            <i class="fa fa-thumbs-up fa-stack-1x fa-inverse"></i>
                        </span>
                    </div>
                </div>
                <div class="post-footer">
                    <Button as='div' onClick={this.handleLikePost.bind(this)} labelPosition='right'>
                        <Button color="red">
                            <Icon name="heart" />
                        </Button>
                        <Label as='a' basic_color="red" pointing='left'>
                            {this.props.post.likes_count}
                        </Label>
                    </Button>
                    <Button as='div' labelPosition='right'>
                        <Button color="blue">
                            <Icon name="thumbs down" />
                            Dislike
                                    </Button>
                        <Label as='a' basic_color="blue" pointing='left'>
                            {this.props.post.dislikes_count}
                        </Label>
                    </Button>
                </div>
            </Fragment>
        )
    }
}

const mapStateToProps = state => ({
    posts: state.posts.posts
});

export default connect(
    null,
    {likePost}
)(PostDetail);
