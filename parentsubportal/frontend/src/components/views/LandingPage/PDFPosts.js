import React, { Fragment, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Item, Label } from "semantic-ui-react";
import PDFDetail from "./PDFDetail";
import { getPDFs } from "../../../actions/pdfs";
import Comments from "./Comments";

function PDFPosts() {
    const dispatch = useDispatch();
    const pdfs = useSelector((state) => state.pdfs.pdfs);

    useEffect(() => {
        dispatch(getPDFs());
    }, [dispatch]);

    return (
        <Fragment>
            <br />
            {pdfs.map((pdf) => (
                <Item.Group>
                    <PDFDetail post={pdf} />
                </Item.Group>
            ))}
        </Fragment>
    );
}

export default PDFPosts;
