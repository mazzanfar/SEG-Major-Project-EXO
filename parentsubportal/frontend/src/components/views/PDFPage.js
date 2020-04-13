import React, { Component, useEffect } from "react";
import { connect, useDispatch, useSelector } from "react-redux";
import PropTypes from "prop-types";
import { getPDF } from "../../actions/pdfs";
import PDFDetail from "./LandingPage/PDFDetail";
import { Item } from "semantic-ui-react";

function PDFPage(props) {
    const pdfId = props.match.params.paramId;
    const pdf = useSelector((state) => state.pdfs.pdf);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getPDF(pdfId));
    }, [dispatch]);

    return post ? (
        <Item.Group>
            <PDFDetail post={pdf} />
        </Item.Group>
    ) : null;
}
export default PDFPage;
