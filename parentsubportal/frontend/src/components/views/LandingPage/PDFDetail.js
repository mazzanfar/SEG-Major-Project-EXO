import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import { Dropdown, Button, Icon, Label, Item, Rating } from "semantic-ui-react";
import PropTypes from "prop-types";
import { getUser } from "../../../actions/auth";
import Comments from "./Comments";

export class PDFDetail extends Component {
    static propTypes = {
        post: PropTypes.array.isRequired,
    };

    state = {
        likes: this.props.post.likes_count,
        dislikes: this.props.post.dislikes_count,
        options: [
            { key: "edit", icon: "edit", text: "Edit Post", value: "edit" },
            {
                key: "delete",
                icon: "delete",
                text: "Remove Post",
                value: "delete",
            },
            { key: "hide", icon: "hide", text: "Hide Post", value: "hide" },
        ],
    };

    /*
    handleLikePost() {
        const like = {"post": this.props.post.id, "user": 14, "vote_type": "like"}
        this.props.likePost(like)
    }
    */

    checkRating = (event, data) => {
        console.log(data.rating);
    };

    render() {
        return (
            <Fragment>
                <Item>
                    <Item.Image
                        size="tiny"
                        src="https://react.semantic-ui.com/images/wireframe/image.png"
                    />
                    <Item.Content>
                        <Item.Header as="a">Header</Item.Header>
                        <Item.Meta>Posted by tom</Item.Meta>
                        <Item.Description>
                            {this.props.post.content}
                        </Item.Description>
                        <Item.Extra>
                            {this.props.post.topics.map((topic) => (
                                <Label href={"/topic/" + topic.name}>
                                    {topic.name}
                                </Label>
                            ))}
                            <Button.Group floated="right" color="teal">
                                <Button>Save</Button>
                                <Dropdown
                                    className="button icon"
                                    floating
                                    options={this.state.options}
                                    trigger={<React.Fragment />}
                                />
                            </Button.Group>
                        </Item.Extra>
                        <Rating
                            maxRating={5}
                            defaultRating={3}
                            onRate={this.checkRating}
                            icon="star"
                            size="tiny"
                        />
                    </Item.Content>
                </Item>
            </Fragment>
        );
    }
}

function mapStateToProps(state, ownProps) {
    return {
        post: state.posts.posts.find((p) => p.id == ownProps.postId),
    };
}

export default connect(mapStateToProps, null)(PostDetail);
