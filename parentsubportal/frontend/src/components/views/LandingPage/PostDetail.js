import React, {Component, Fragment} from "react";
import {connect} from "react-redux";
import {Dropdown, Button, Icon, Label, Item, Rating} from "semantic-ui-react";
import {likePost} from "../../../actions/likes"
import PropTypes from "prop-types";

export class PostDetail extends Component {

    static propTypes = {
        post: PropTypes.array.isRequired
    };

    state = {
        likes: this.props.post.likes_count,
        dislikes: this.props.post.dislikes_count,
        options: [
          { key: 'edit', icon: 'edit', text: 'Edit Post', value: 'edit' },
          { key: 'delete', icon: 'delete', text: 'Remove Post', value: 'delete' },
          { key: 'hide', icon: 'hide', text: 'Hide Post', value: 'hide' },
        ]
    }

    /*
    handleLikePost() {
        const like = {"post": this.props.post.id, "user": 14, "vote_type": "like"}
        this.props.likePost(like)
    }

    handleDislikePost() {
        const like = {"post": this.props.post.id, "user": 14, "vote_type": "dislike"}
        this.props.likePost(like)
    }
    */

    checkRating = (event, data) => {
        console.log(data.rating)
    }

    render() {
        return (
            <Item>
                <Item.Image size='tiny' src='https://react.semantic-ui.com/images/wireframe/image.png' />
                <Item.Content>
                    <Item.Header as='a'>Header</Item.Header>
                    <Item.Meta>Posted by tom</Item.Meta>
                    <Item.Description>
                        {this.props.post.content}
                    </Item.Description>
                    <Item.Extra>
                        <Label>Autism</Label>
                        <Label>Something</Label>
                        <Button.Group floated="right" color='teal'>
                            <Button>Save</Button>
                            <Dropdown
                              className='button icon'
                              floating
                              options={this.state.options}
                              trigger={<React.Fragment />}
                            />
                        </Button.Group>
                    </Item.Extra>
                <Rating maxRating={5} defaultRating={3} onRate={this.checkRating} icon='star' size='tiny' />
                </Item.Content>
            </Item>
        )
    }
}

function mapStateToProps(state, ownProps) {
    return {
    post: state.posts.posts.find(p => p.id == ownProps.postId)
    };
}

export default connect(
    mapStateToProps,
    {likePost}
)(PostDetail);
