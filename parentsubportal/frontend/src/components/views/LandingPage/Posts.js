import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPosts } from "../../../actions/posts";
import Comments from "./comments"
import './styles.scss'

export class Posts extends Component {
    static propTypes = {
        posts: PropTypes.array.isRequired,
        getPosts: PropTypes.func.isRequired,
        //deletePost: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getPosts();
    }

    render() {
        return (
          <Fragment>
                <br />
                <div class="container">
                        <div class="post">
                        {this.props.posts.map(post => (
                            <div class="post-body">
                                
                            <div class="post-header">
                               <span class="userimage"><img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt=""/></span>
                               <span class="username"><a href="javascript:;">John Smith</a> <small></small></span>
                               <span class="float-right text-muted">{post.views} Views</span>
                            </div>
                            <div class="post-content">
                               <p>
                                    {post.content}
                               </p>
                            </div>
                            <div class="post-likes">
                               <div class="stats-right">
                                  <span class="stats-text">{}</span>
                                  <span class="stats-text">{post.total_comments} Comments</span>
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
                                  <span class="stats-total">4.3k</span>
                               </div>
                            </div>
                            <div class="post-footer">
                               <a href="javascript:;" class="m-r-15 text-inverse-lighter"><i class="fa fa-thumbs-up fa-fw fa-lg m-r-3"></i> Like</a>
                               <a href="javascript:;" class="m-r-15 text-inverse-lighter"><i class="fa fa-comments fa-fw fa-lg m-r-3"></i> Comment</a> 
                               <a href="javascript:;" class="m-r-15 text-inverse-lighter"><i class="fa fa-share fa-fw fa-lg m-r-3"></i> Share</a>
                            </div>
                            <Comments post={post}/>
                            </div>
                        ))}
                        </div>
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
    { getPosts }
)(Posts);
