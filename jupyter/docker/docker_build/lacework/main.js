// Code cell snippets

define([
    'base/js/namespace',
], function(
    Jupyter,
) {
    "use strict";

    // will be called when the nbextension is loaded
    function load_extension() {
        var ncells = Jupyter.notebook.ncells();
        if (ncells > 1) {
          return true;
        }

        var new_cell = Jupyter.notebook.insert_cell_above('markdown', 0);
        new_cell.set_text('# Lacework Notebook\nChange this text to reflect what this notebook attempts to accomplish.\n**Remember to rename the notebook itself as well**.');
        new_cell.render();
        new_cell.focus_cell();

        var import_cell = Jupyter.notebook.insert_cell_below('code');
        import_cell.set_text('client = lw.get_client()');

        var new_cell = Jupyter.notebook.insert_cell_below('markdown');
        new_cell.set_text('## Connecting to Lacework\nBasic imports have already been completed, we now need to connect to the Lacework API using the Jupyter helper.\nExecute the cell below by pressing the play button or using "shift + enter"\n\nAlll Lacework SDK actions happen on either the lw object or the client, which can be gathered using the lw.get_client() function.');
        new_cell.render();
        import_cell.focus_cell();
    };

    // return public methods
    return {
        load_ipython_extension : load_extension
    };
});
