<%
    from alembic.autogenerate import comparators
    @comparators.dispatch_for("schema")
    def compare_schemas(autogen_context, upgrade_ops, schema_names):
        if None in schema_names:
            return False
        else:
            return True
%>