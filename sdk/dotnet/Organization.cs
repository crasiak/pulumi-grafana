// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Grafana
{
    public partial class Organization : Pulumi.CustomResource
    {
        [Output("adminUser")]
        public Output<string?> AdminUser { get; private set; } = null!;

        [Output("admins")]
        public Output<ImmutableArray<string>> Admins { get; private set; } = null!;

        [Output("createUsers")]
        public Output<bool?> CreateUsers { get; private set; } = null!;

        [Output("editors")]
        public Output<ImmutableArray<string>> Editors { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("orgId")]
        public Output<int> OrgId { get; private set; } = null!;

        [Output("viewers")]
        public Output<ImmutableArray<string>> Viewers { get; private set; } = null!;


        /// <summary>
        /// Create a Organization resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Organization(string name, OrganizationArgs? args = null, CustomResourceOptions? options = null)
            : base("grafana:/organization:Organization", name, args ?? new OrganizationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Organization(string name, Input<string> id, OrganizationState? state = null, CustomResourceOptions? options = null)
            : base("grafana:/organization:Organization", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Organization resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Organization Get(string name, Input<string> id, OrganizationState? state = null, CustomResourceOptions? options = null)
        {
            return new Organization(name, id, state, options);
        }
    }

    public sealed class OrganizationArgs : Pulumi.ResourceArgs
    {
        [Input("adminUser")]
        public Input<string>? AdminUser { get; set; }

        [Input("admins")]
        private InputList<string>? _admins;
        public InputList<string> Admins
        {
            get => _admins ?? (_admins = new InputList<string>());
            set => _admins = value;
        }

        [Input("createUsers")]
        public Input<bool>? CreateUsers { get; set; }

        [Input("editors")]
        private InputList<string>? _editors;
        public InputList<string> Editors
        {
            get => _editors ?? (_editors = new InputList<string>());
            set => _editors = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("viewers")]
        private InputList<string>? _viewers;
        public InputList<string> Viewers
        {
            get => _viewers ?? (_viewers = new InputList<string>());
            set => _viewers = value;
        }

        public OrganizationArgs()
        {
        }
    }

    public sealed class OrganizationState : Pulumi.ResourceArgs
    {
        [Input("adminUser")]
        public Input<string>? AdminUser { get; set; }

        [Input("admins")]
        private InputList<string>? _admins;
        public InputList<string> Admins
        {
            get => _admins ?? (_admins = new InputList<string>());
            set => _admins = value;
        }

        [Input("createUsers")]
        public Input<bool>? CreateUsers { get; set; }

        [Input("editors")]
        private InputList<string>? _editors;
        public InputList<string> Editors
        {
            get => _editors ?? (_editors = new InputList<string>());
            set => _editors = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("orgId")]
        public Input<int>? OrgId { get; set; }

        [Input("viewers")]
        private InputList<string>? _viewers;
        public InputList<string> Viewers
        {
            get => _viewers ?? (_viewers = new InputList<string>());
            set => _viewers = value;
        }

        public OrganizationState()
        {
        }
    }
}
